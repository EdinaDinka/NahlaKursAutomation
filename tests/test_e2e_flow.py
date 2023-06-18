from pages.home_page import HomePage
from pages.products_page import ProductsPage
from pages.cart_page import CartPage

def test_e2e_flow(driver):
    home_page = HomePage(driver)
    home_page.go_to()
    home_page.login("standard_user", "secret_sauce")
    products_page = ProductsPage(driver)
    assert products_page.is_at_page() == "Products"

   # products_page.add_items(2)
    products_page.open_cart()

    cart_page = CartPage(driver)
    assert cart_page.is_at_page() == "Your Cart"

    


    