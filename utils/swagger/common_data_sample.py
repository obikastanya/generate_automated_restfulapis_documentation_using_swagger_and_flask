from dataclasses import dataclass
from http.client import responses


@dataclass
class Response:
    default_message = "Message"
    http_responses = responses
