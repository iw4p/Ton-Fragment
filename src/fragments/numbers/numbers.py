try:
    from ..helpers.server import *
except ImportError:
    from .helpers.server import *

class Numbers:
    """ Numbers model
    """
    def __init__(self, status: str, sort: str, count: int):
        self.status = status
        self.sort = sort
        self.count = count

    @property
    def func(self) -> str:
        return 

    def res(self):
        print(get_html_content_from_page())

    # TODO
    # def to_json(self) -> dict:
    #     return {
    #         self.count: {
    #             'info': self.info,
    #         }
    #     }
    
    # TODO
    # def assemble_simple_text(self) -> str:
    #     return (
    #         f'{self.test}: ',
    #         '\n'
    #     )
