
class ComparisonError(Exception):
  def __init__(self, obj1, obj2):
    super().__init__(f"You can not compare a {obj1.__class__.__name__} with {obj2.__class__.__name__}")