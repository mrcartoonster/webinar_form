import re

from flask_wtf import FlaskForm
from wtforms import (
    EmailField,
    SelectField,
    StringField,
    SubmitField,
    TelField,
)
from wtforms.validators import (
    DataRequired,
    Email,
    Length,
    Optional,
    ValidationError,
)


def zip_code(form, field):
    """
    This validates US and Canadian postal/zip codes
    :param form:
    :param field:
    :return:
    """
    us = re.compile(r"^\d{5}(?:[-\s]\d{4})?$")

    us_zip = us.search(field.data)
    if us_zip is not None:
        raise ValidationError(
            message="You need to input a valid US Zip Code!",
        )


class WebinarForm(FlaskForm):
    name = StringField(
        "Name",
        validators=[
            DataRequired(message="Enter first name"),
            Length(max=20),
        ],
    )
    last_name = StringField(
        "Last Name",
        validators=[
            DataRequired(message="Enter the last name"),
            Length(max=30),
        ],
    )
    email = EmailField(
        "Email",
        validators=[
            DataRequired(message="Enter Email address"),
            Email(message="Most be valid email"),
        ],
    )
    work_phone = TelField(
        "Work Phone",
        validators=[DataRequired(message="Enter your work phone")],
    )
    company = StringField(
        "Company",
        validators=[
            DataRequired(message="Please enter company name"),
            Length(max=30),
        ],
    )
    company_address = StringField(
        "Company Address",
        validators=[DataRequired(message="Enter Street Address")],
    )
    street_address = StringField(
        "Street Address Line 2",
        validators=[Optional()],
    )
    city = StringField(
        "City",
        validators=[DataRequired(message="Please enter the city")],
    )
    state = StringField(
        "State",
        validators=[DataRequired(message="Please enter the city")],
    )
    postal = StringField(
        "Zip Code",
        validators=[
            DataRequired("Enter your postal or zip code."),
            zip_code,
        ],
    )
    country = SelectField(
        "Country",
        choices=["US", "Canada"],
        validators=[DataRequired(message="Select Country")],
    )
    website = StringField(
        "Company Website",
        validators=[
            DataRequired(message="Please enter you company website."),
        ],
    )
    submit = SubmitField("Submit")
