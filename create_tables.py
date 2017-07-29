from upload.database import engine
from upload.models import Base

Base.metadata.create_all(engine)