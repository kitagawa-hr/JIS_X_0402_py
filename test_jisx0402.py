import pytest

import jisx0402
from jisx0402 import Record


class TestRecord:
    def test_attrs(self):
        obj = jisx0402.RECORDS[0]
        for attr in obj.attrs:
            assert hasattr(obj, attr)

    def test_full_city_name(self):
        hokkaido = jisx0402.RECORDS[0]
        assert hokkaido.full_city_name == "北海道"
        sapporo = jisx0402.RECORDS[1]
        assert sapporo.full_city_name == "北海道札幌市"

    def test_full_city_kana(self):
        hokkaido = jisx0402.RECORDS[0]
        assert hokkaido.full_city_name_kana == "ﾎｯｶｲﾄﾞｳ"
        sapporo = jisx0402.RECORDS[1]
        assert sapporo.full_city_name_kana == "ﾎｯｶｲﾄﾞｳｻｯﾎﾟﾛｼ"


@pytest.mark.parametrize(
    "code,record",
    [
        (
            "010006",
            jisx0402.Record(code="010006", prefecture="北海道", prefecture_kana="ﾎｯｶｲﾄﾞｳ", city="", city_kana=""),
        ),
        (
            "10006",
            jisx0402.Record(code="010006", prefecture="北海道", prefecture_kana="ﾎｯｶｲﾄﾞｳ", city="", city_kana=""),
        ),
        (
            10006,
            jisx0402.Record(code="010006", prefecture="北海道", prefecture_kana="ﾎｯｶｲﾄﾞｳ", city="", city_kana=""),
        ),
        (
            "011002",
            jisx0402.Record(code="011002", prefecture="北海道", prefecture_kana="ﾎｯｶｲﾄﾞｳ", city="札幌市", city_kana="ｻｯﾎﾟﾛｼ"),
        ),
        (
            "082112",
            jisx0402.Record(
                code="082112", prefecture="茨城県", prefecture_kana="ｲﾊﾞﾗｷｹﾝ", city="常総市", city_kana="ｼﾞｮｳｿｳｼ"
            ),
        ),
        (
            "205907",
            jisx0402.Record(code="205907", prefecture="長野県", prefecture_kana="ﾅｶﾞﾉｹﾝ", city="飯綱町", city_kana="ｲｲﾂﾞﾅﾏﾁ"),
        ),
    ],
)
def test_code2record(code, record):
    assert jisx0402.code2record(code) == record


@pytest.mark.parametrize(
    "key, pattern, result",
    [
        (
            "full_city_name",
            r"福.県$",
            [
                Record(code="070009", prefecture="福島県", prefecture_kana="ﾌｸｼﾏｹﾝ", city="", city_kana=""),
                Record(code="180009", prefecture="福井県", prefecture_kana="ﾌｸｲｹﾝ", city="", city_kana=""),
                Record(code="400009", prefecture="福岡県", prefecture_kana="ﾌｸｵｶｹﾝ", city="", city_kana=""),
            ],
        ),
        (
            "city",
            r"姫.*",
            [
                Record(code="282014", prefecture="兵庫県", prefecture_kana="ﾋｮｳｺﾞｹﾝ", city="姫路市", city_kana="ﾋﾒｼﾞｼ"),
                Record(code="443221", prefecture="大分県", prefecture_kana="ｵｵｲﾀｹﾝ", city="姫島村", city_kana="ﾋﾒｼﾏﾑﾗ"),
            ],
        ),
        (
            "city_kana",
            r"ｱｷ",
            [
                Record(code="052019", prefecture="秋田県", prefecture_kana="ｱｷﾀｹﾝ", city="秋田市", city_kana="ｱｷﾀｼ"),
                Record(code="132071", prefecture="東京都", prefecture_kana="ﾄｳｷｮｳﾄ", city="昭島市", city_kana="ｱｷｼﾏｼ"),
                Record(code="132284", prefecture="東京都", prefecture_kana="ﾄｳｷｮｳﾄ", city="あきる野市", city_kana="ｱｷﾙﾉｼ"),
                Record(code="342149", prefecture="広島県", prefecture_kana="ﾋﾛｼﾏｹﾝ", city="安芸高田市", city_kana="ｱｷﾀｶﾀｼ"),
                Record(code="343684", prefecture="広島県", prefecture_kana="ﾋﾛｼﾏｹﾝ", city="安芸太田町", city_kana="ｱｷｵｵﾀﾁｮｳ"),
                Record(code="392031", prefecture="高知県", prefecture_kana="ｺｳﾁｹﾝ", city="安芸市", city_kana="ｱｷｼ"),
            ],
        ),
    ],
)
def test_search(key, pattern, result):
    assert jisx0402.search(key, pattern) == result
