from model.product_model import ProductCreate

class ProductService:
    async def find_product_by_id(self, id: str):
        return "product"
    
    async def create_product(self, product: ProductCreate):
        return "added product"