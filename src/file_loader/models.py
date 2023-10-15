from sqlalchemy import Column
from sqlalchemy import MetaData
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.schema import ForeignKey
from sqlalchemy_file import ImageField
from sqlalchemy_file.storage import StorageManager
from libcloud.storage.drivers.local import LocalStorageDriver

from src.models import User
from src.database import Base
from .utils import Image


metadata = MetaData()


class Cover(Base, Image):
    metadata = metadata
    __tablename__ = 'Cover'
    owner: Mapped[int] = mapped_column(ForeignKey(User.id))
    file: Mapped[str] = mapped_column(ImageField(upload_storage='covers', thumbnail_size=(200, 265)))


class Attachment(Base, Image):
    metadata = metadata
    __tablename__ = 'Attachment'
    owner: Mapped[int] = mapped_column(ForeignKey(User.id))
    file: Mapped[str] = mapped_column(ImageField(upload_storage='attachments'))


class UserIcon(Base, Image):
    metadata = metadata
    __tablename__ = 'UserIcon'
    owner: Mapped[int] = mapped_column(ForeignKey(User.id))
    file: Mapped[str] = mapped_column(ImageField(upload_storage='user_icons', thumbnail_size=(80, 80)))




user_icons_container = LocalStorageDriver('./static').get_container('user_icons_container')
covers_container = LocalStorageDriver('./static').get_container('covers')
attachments_container = LocalStorageDriver('./static').get_container('attachments')
StorageManager.add_storage('covers', covers_container)
StorageManager.add_storage('attachments', attachments_container)
StorageManager.add_storage('user_icons', user_icons_container)
