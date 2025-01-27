

class LocationMetadata:
    def __init__(self, data: dict):
        self.data: dict = data
        self.consent_required: bool = data.get("consent_required")
        self.country_code: str = data.get("country_code")
        self.promotional_email_opt_in: PromotionalEmailOptIn = PromotionalEmailOptIn(data.get("promotional_email_opt_in", {}))


class PromotionalEmailOptIn:
    def __init__(self, data: dict):
        self.data: dict = data
        self.required: bool = data.get("required")
        self.pre_checked: bool = data.get("pre_checked")