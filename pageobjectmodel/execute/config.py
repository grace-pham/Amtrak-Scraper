class Config:
    # url
    baseUrl = "https://www.amtrak.com/"
    homepageUrl = baseUrl + "home.html"
    ticketInfoUrl = baseUrl + "tickets/departure.html"

    # selector home page

    input_origin_field_CSS = "#page-content  .amtrak-ff-body .from-station input"
    input_destination_field_CSS = "#mat-input-1"
    input_departure_date_CSS = "#mat-input-2"
    origin_dropdown_CSS = "#autocomplete__0 div:nth-child(1) > div.am-dropdown__option.am-simple-dropdown__option.ng-star-inserted"
    destination_dropdown_CSS = "#autocomplete__1 > div > div > div:nth-child(1) > div:nth-child(2)"
    search_train_button_CSS = "button.search-btn.ng-star-inserted"

    # selector ticket info page
    train_number_list = "train-info span:nth-child(1)"
    departure_time_list = "div.departure .departure-details span.font-light"
    arrival_time_list = ".arrival .departure-details span.font-light"