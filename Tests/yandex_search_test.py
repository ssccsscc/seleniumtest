import pytest
from PageObjects.yandex_search_form import YandexSearchForm
from PageObjects.yandex_modal import YandexModal
from PageObjects.yandex_search_result import YandexSearchResult
from PageObjects.yandex_search_results import YandexSearchResults


@pytest.mark.dependency()
def test_yandex_search_suggestions(driver):
    driver.get("https://yandex.ru/")

    yandex_modal = YandexModal(driver)
    if yandex_modal.is_modal_present():
        yandex_modal.close_modal()

    yandex_search = YandexSearchForm(driver)
    yandex_search.input_into_search("Тензор")
    assert len(yandex_search.get_suggestions_texts()) > 0


@pytest.mark.dependency(depends=["test_yandex_search_suggestions"])
def test_yandex_search_results(driver):
    yandex_search = YandexSearchForm(driver)
    yandex_search.search_using_enter()
    yandex_search.wait_till_page_changed()

    search_results = YandexSearchResults(driver).get_items()
    assert len(search_results) > 0

    search_top_result = YandexSearchResult(driver, search_results[0])
    assert search_top_result.get_link() == 'https://tensor.ru/'
