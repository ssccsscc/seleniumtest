import pytest
from PageObjects.yandex_images_popular_requests import YandexImagesPopularRequests
from PageObjects.yandex_media_viewer import YandexMediaViewer
from PageObjects.yandex_search_form import YandexSearchForm
from PageObjects.yandex_modal import YandexModal
from PageObjects.yandex_search_result import YandexSearchResult
from PageObjects.yandex_search_results import YandexSearchResults
from PageObjects.yandex_services import YandexServices
from urllib.parse import urlsplit, urlunsplit


@pytest.mark.dependency()
def test_images_link(driver):
    driver.get("https://yandex.ru/")

    yandex_modal = YandexModal(driver)
    if yandex_modal.is_modal_present():
        yandex_modal.close_modal()

    yandex_services = YandexServices(driver)

    assert "Картинки" in yandex_services.get_link_names(), "Нету ссылки на картинки в меню"

    yandex_services.click_on_link_by_name("Картинки")
    yandex_services.wait_till_window_opened()
    yandex_services.switch_to_window(-1)

    YandexImagesPopularRequests(driver)

    assert urlunsplit(urlsplit(yandex_services.driver.current_url)._replace(query="", fragment="")) == "https://yandex.ru/images/", "Перешли не на https://yandex.ru/images/"


@pytest.mark.dependency(depends=["test_images_link"])
def test_images_category(driver):
    yandex_popular = YandexImagesPopularRequests(driver)

    first_link_text = yandex_popular.get_link_names()[0]
    yandex_popular.click_on_link_by_name(first_link_text)

    YandexSearchResults(driver)

    assert YandexSearchForm(driver).get_search_text() == first_link_text, "Название категории не совпадает"


@pytest.mark.dependency(depends=["test_images_category"])
def test_images_viewer(driver):
    results = YandexSearchResults(driver)
    first_result = YandexSearchResult(driver, results.get_items()[0])
    first_result.click_link()

    media_viewer = YandexMediaViewer(driver)
    first_img = media_viewer.get_current_img_src()

    media_viewer.next_img()
    assert media_viewer.get_current_img_src() != first_img, "Кнопка вперед не меняет картинку"

    media_viewer.prev_img()
    assert media_viewer.get_current_img_src() == first_img, "Кнопка назад не меняет картинку"
