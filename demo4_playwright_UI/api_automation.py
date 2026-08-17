from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    api_context=p.request.new_context(base_url="https://petstore.swagger.io/v2/")

    response=api_context.get("pet/5")
    print(response.status)
    print(response.status_text)
    print(response.headers)
    print(response.headers["date"])
    print(response.text())
    print(response.json())
    print(response.json()["id"])
    print(response.json()["name"])
    print(response.json()["status"])
    print(response.json()["category"]["id"])
    print(response.json()["category"]["name"])

    response_body=response.json()

    print(response_body["tags"])
    print(response_body["tags"][0])
    print(response_body["tags"][0]["id"])

