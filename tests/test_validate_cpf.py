import random

from src.validate_cnpj import validate_cnpj

VALID_CNPJ_LIST_WITH_MASK = [
    '40.858.686/0001-70',
    '02.704.359/0001-75',
    '45.977.850/0001-82',
    '99.222.415/0001-77',
    '03.337.588/0001-61',
]
VALID_CNPJ_LIST_WITHOUT_MASK = [
    '40858686000170',
    '02704359000175',
    '45977850000182',
    '99222415000177',
    '03337588000161',
]
INVALID_CNPJ_LIST_WITH_MASK = [
    '40.158.686/0001-70',
    '02.104.359/0001-75',
    '45.177.850/0001-82',
    '99.122.415/0001-77',
    '03.137.588/0001-61',
]
INVALID_CNPJ_LIST_WITHOUT_MASK = [
    '40158686000170',
    '02104359000175',
    '45177850000182',
    '99122415000177',
    '03137588000161',
]

VALID_CNPJ_WITH_MASK = random.choice(VALID_CNPJ_LIST_WITH_MASK)
VALID_CNPJ_WITHOUT_MASK = random.choice(VALID_CNPJ_LIST_WITHOUT_MASK)

INVALID_CNPJ_WITH_MASK = random.choice(INVALID_CNPJ_LIST_WITH_MASK)
INVALID_CNPJ_WITHOUT_MASK = random.choice(INVALID_CNPJ_LIST_WITHOUT_MASK)


def test_validate_cnpj_module():
    assert validate_cnpj is not None


def test_clean_cnpj():
    clened_cnpj = validate_cnpj._clean(INVALID_CNPJ_WITH_MASK)
    assert all(i.isdigit() == True for i in clened_cnpj)
    clened_cnpj = validate_cnpj._clean(VALID_CNPJ_WITH_MASK)
    assert all(i.isdigit() == True for i in clened_cnpj)


def test_correct_cnpj_length():
    assert validate_cnpj._has_correct_length(VALID_CNPJ_WITHOUT_MASK) == True


def test_incorrect_cnpj_length():
    SMALLER_CNPJ = '2418751700012'
    assert validate_cnpj._has_correct_length(SMALLER_CNPJ) == False
    BIGGER_CNPJ = '241875170001231'
    assert validate_cnpj._has_correct_length(BIGGER_CNPJ) == False


def test_is_not_allowed_cnpj():
    ALLOWED_cnpj = '11111111111'
    assert validate_cnpj._is_allowed(ALLOWED_cnpj) == False


def test_is_allowed_cnpj():
    assert validate_cnpj._is_allowed(VALID_CNPJ_WITHOUT_MASK) == True


def test_fist_verification_digit():
    CORRECT_FIST_DIGIT = int(VALID_CNPJ_WITHOUT_MASK[-2])
    assert validate_cnpj._caculate_digit(VALID_CNPJ_WITHOUT_MASK) == CORRECT_FIST_DIGIT


def test_last_verification_digit():
    CORRECT_LAST_DIGIT = int(VALID_CNPJ_WITHOUT_MASK[-1])
    assert (
        validate_cnpj._caculate_digit(VALID_CNPJ_WITHOUT_MASK, is_first_digit=False)
        == CORRECT_LAST_DIGIT
    )


def test_invalid_cnpj_whitout_mask():
    CNPJ = INVALID_CNPJ_WITHOUT_MASK
    assert validate_cnpj.is_valid(CNPJ) == False


def test_invalid_cnpj_with_mask():
    CNPJ = INVALID_CNPJ_WITH_MASK
    assert validate_cnpj.is_valid(CNPJ) == False


def test_valid_cnpj_whitout_mask():
    CNPJ = VALID_CNPJ_WITHOUT_MASK
    assert validate_cnpj.is_valid(CNPJ) == True


def test_valid_cnpj_with_mask():
    CNPJ = VALID_CNPJ_WITH_MASK
    assert validate_cnpj.is_valid(CNPJ) == True


def test_all_invalid_cnpj_with_mask():
    for CNPJ in INVALID_CNPJ_LIST_WITH_MASK:
        assert validate_cnpj.is_valid(CNPJ) == False


def test_all_invalid_cnpj_without_mask():
    for CNPJ in INVALID_CNPJ_LIST_WITHOUT_MASK:
        assert validate_cnpj.is_valid(CNPJ) == False


def test_all_valid_cnpj_with_mask():
    for CNPJ in VALID_CNPJ_LIST_WITH_MASK:
        assert validate_cnpj.is_valid(CNPJ) == True


def test_all_valid_cnpj_without_mask():
    for CNPJ in VALID_CNPJ_LIST_WITHOUT_MASK:
        assert validate_cnpj.is_valid(CNPJ) == True
