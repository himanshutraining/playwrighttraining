from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    api_context=p.request.new_context(base_url="https://petstore.swagger.io/v2/")

    response=api_context.get("pet/findByStatus?status=sold")

    print(response.status)

    print(response.json()[2]["status"])

    