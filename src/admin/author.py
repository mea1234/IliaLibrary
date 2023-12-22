from src.config import Config
from flask_admin.contrib.sqla import ModelView
from flask_admin.form.upload import ImageUploadField
from flask_admin.model.template import BaseListRowAction, LinkRowAction



class ViewRowAction(LinkRowAction):

    def __init__(self, icon_class, url = None):
        super(ViewRowAction, self).__init__(icon_class, url)



    def render(self, context, row_id, row):
        n = self._resolve_symbol(context, 'row_actions.link')
        return n(self, f"/book/{row.id}")
       

class AuthorView(ModelView):

    column_extra_row_actions = [ViewRowAction("fa fa-eye")]

    column_default_sort = ("created_at", True)

    page_size = 15

    column_labels = {"name" : "სახელი", "last_name" : "გვარი", "book_count" : "წიგნების რაოდენობა"}

    column_list = ["name", "last_name", "book_count"]

    column_searchable_list = ["name", "last_name"]

    form_columns = ["name", "last_name"]