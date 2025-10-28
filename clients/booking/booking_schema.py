from datetime import date

from pydantic import BaseModel, Field
from tools.fakers import fake

class Dates(BaseModel):
    check_in: str = Field(alias="checkin", default='2018-09-09')
    check_out: str = Field(alias="checkout", default='2019-09-09')


class BookingSchema(BaseModel):
    first_name: str = Field(alias="firstname")
    lastname: str = Field(alias="lastname")
    total_price: int = Field(alias="totalprice")
    deposit_paid: bool = Field(alias="depositpaid")
    booking_dates: Dates = Field(alias="bookingdates")
    additional_needs: str = Field(alias="additionalneeds")


class CreateBookingRequestSchema(BaseModel):
    first_name: str = Field(alias="firstname", default_factory=fake.first_name)
    lastname: str = Field(alias="lastname", default_factory=fake.last_name)
    total_price: int = Field(alias="totalprice", default_factory=fake.integer)
    deposit_paid: bool = Field(alias="depositpaid", default=True)
    booking_dates: Dates = Field(alias="bookingdates",default_factory=Dates)
    additional_needs: str = Field(alias="additionalneeds", default="Breakfast")


class CreateBookingResponseSchema(BaseModel):
    booking_id: int = Field(alias="bookingid")
    booking: CreateBookingRequestSchema


class UpdateBoookingRequestSchema(BaseModel):
    first_name: str | None = Field(alias="firstname", default_factory=fake.first_name)
    lastname: str | None = Field(alias="lastname", default_factory=fake.last_name)
    total_price: int | None = Field(alias="totalprice", default_factory=fake.integer)
    deposit_paid: bool | None = Field(alias="depositpaid", default=True)
    booking_dates: Dates | None = Field(alias="bookingdates", default_factory=Dates)
    additional_needs: str | None = Field(alias="additionalneeds", default="Lanch")


class UpdateResponseBookingSchema(BaseModel):
    booking: BookingSchema

