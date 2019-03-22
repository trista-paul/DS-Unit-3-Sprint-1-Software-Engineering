from random import randint, sample, uniform
from acme import Product


ADJECTIVES = ['Awesome ', 'Shiny ', 'Impressive ', 'Portable ', 'Improved ']
NOUNS = ['Anvil', 'Catapult', 'Disguise', 'Mousetrap', '???']


def generate_products(n=30):
   '''
   generates a list of n (default 30) products compatible with the Products class
   '''
    products = []
    for prod in range(n):
        name = random.choice(ADJECTIVES) + random.choice(NOUNS)
        price = random.randint(5, 100)
        weight = random.randint(5, 100)
        flammability = random.uniform(0.0, 2.5)
        prod = [name, price, weight, flammability]
        products.append(prod)
    return products


def inventory_report(products):
  '''
  prints the number of unique products and the average price, weight and flammability
  of the list of products made by generate_products
  '''
  print('ACME CORPORATION OFFICIAL INVENTORY REPORT')
  names = []
  price = []
  weight = []
  flammability = []
  for prod in products:
    names.append(prod[0])
    price.append(prod[1])
    weight.append(prod[2])
    flammability.append(prod[3])
  unique_names = []
  for name in names:
    if name not in unique_names:
      unique_names.append(name)
  nunique = len(unique_names)
  avgprice = sum(price) / len(price)
  avgweight = sum(weight) / len(weight)
  avgflamm = sum(flammability) / len(flammability)
  print('Unique products: '+str(nunique))
  print('Average price: '+str(avgprice))
  print('Average weight: '+str(avgweight))
  print('Average flammability: ' +str(avgflamm))
  pass
          
  '''runs inventory report by calling file'''
  if __name__ == '__main__':
      inventory_report(generate_products())
  
    
