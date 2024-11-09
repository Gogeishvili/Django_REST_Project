from django.db import models
from django.forms.models import model_to_dict
from django.conf import settings


class ProductManager(models.Manager):

    def get_prodacts_JSON_data(self):
        products = self.all().prefetch_related("categories", "tags")
        products_data = []
        for pro in products:
            product = {
                "id": pro.id,
                "name": pro.name,
                "title": pro.title,
                "price": str(pro.price),
                "quantity": pro.quantity,
                "is_active": pro.is_active,
                "slug": pro.slug,
                "created_at": pro.created_at.isoformat(),
                "updated_at": pro.updated_at.isoformat(),
                "categories": [model_to_dict(cat) for cat in pro.categories.all()],
                "tags": [model_to_dict(tag) for tag in pro.tags.all()],
            }
            if pro.image:
                product["image_url"] = settings.MEDIA_URL + pro.image.url
            else:
                product["image_url"] = None
            products_data.append(product)

        return products_data


class CategoryManager(models.Manager):

    def get_category_JSON_data(self):
        categories = self.all().prefetch_related("products")
        categories_data = []
        for cat in categories:
            parent_data = {"id": cat.parent.id, "name": cat.parent.name} if cat.parent else None
            category = {
                "id": cat.id,
                "name": cat.name,
                "parent": parent_data,
                "products": [
                    {
                        "id": pro.id,
                        "name": pro.name,
                        "title": pro.title,
                        "price": str(pro.price),
                        "quantity": pro.quantity,
                        "is_active": pro.is_active,
                        "slug": pro.slug,
                        "created_at": pro.created_at.isoformat(),
                        "updated_at": pro.updated_at.isoformat(),
                        "image_url": pro.image.url if pro.image else None,
                    }
                    for pro in cat.products.all()
                ],
            }
            categories_data.append(category)
        return categories_data
