'''Linear_search_product'''

def linearSearchProduct(productList,targetProduct):
  indices = []

  for index, product in enumerate (productList):
    if product == targetProduct:
      indices.append(index)

  return indices

#Examples usage
products = ["shoes", "boot","Loafer","shoes", "sandal", "shoes"]
target = "shoes"
target2 ='apple'
result = linearSearchProduct(products,target)
print(result)

