import os
import pytest
from chroma_feedback.producer.terraform.core import fetch


def test_fetch_slug() -> None:
	slug = 'tuxco/terraform-cloud-test' # slug = 'redaxmedia/chroma-feedback'

	if 'TFE_TOKEN' in os.environ:
		result = fetch('https://app.terraform.io', slug, os.environ['TFE_TOKEN'])
		assert result[0]['producer'] == 'terraform'
		assert result[0]['slug'] == slug
		assert result[0]['active'] is True
		assert result[0]['status']
		assert result[0]['effect']
	else:
		pytest.skip('TFE_TOKEN is not defined')


def test_fetch_invalid() -> None:
	result = fetch(None, None, None)

	assert result == []
