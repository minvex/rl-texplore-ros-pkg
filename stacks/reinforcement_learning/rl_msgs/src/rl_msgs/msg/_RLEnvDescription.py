"""autogenerated by genpy from rl_msgs/RLEnvDescription.msg. Do not edit."""
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct


class RLEnvDescription(genpy.Message):
  _md5sum = "41ee0d621b8031a958ff6d1f587a3860"
  _type = "rl_msgs/RLEnvDescription"
  _has_header = False #flag to mark the presence of a Header object
  _full_text = """# Message that contains details about an RL enviroment/task
float32 num_actions
float32 num_states

#Optional information to describe the range of a continous state
#Some RL algorithms may need this to discretize the state space
float32[] min_state_range
float32[] max_state_range

#Info needed for r-max some other methods
float32 max_reward
float32 reward_range

bool stochastic
bool episodic
string title

"""
  __slots__ = ['num_actions','num_states','min_state_range','max_state_range','max_reward','reward_range','stochastic','episodic','title']
  _slot_types = ['float32','float32','float32[]','float32[]','float32','float32','bool','bool','string']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       num_actions,num_states,min_state_range,max_state_range,max_reward,reward_range,stochastic,episodic,title

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(RLEnvDescription, self).__init__(*args, **kwds)
      #message fields cannot be None, assign default values for those that are
      if self.num_actions is None:
        self.num_actions = 0.
      if self.num_states is None:
        self.num_states = 0.
      if self.min_state_range is None:
        self.min_state_range = []
      if self.max_state_range is None:
        self.max_state_range = []
      if self.max_reward is None:
        self.max_reward = 0.
      if self.reward_range is None:
        self.reward_range = 0.
      if self.stochastic is None:
        self.stochastic = False
      if self.episodic is None:
        self.episodic = False
      if self.title is None:
        self.title = ''
    else:
      self.num_actions = 0.
      self.num_states = 0.
      self.min_state_range = []
      self.max_state_range = []
      self.max_reward = 0.
      self.reward_range = 0.
      self.stochastic = False
      self.episodic = False
      self.title = ''

  def _get_types(self):
    """
    internal API method
    """
    return self._slot_types

  def serialize(self, buff):
    """
    serialize message into buffer
    :param buff: buffer, ``StringIO``
    """
    try:
      _x = self
      buff.write(_struct_2f.pack(_x.num_actions, _x.num_states))
      length = len(self.min_state_range)
      buff.write(_struct_I.pack(length))
      pattern = '<%sf'%length
      buff.write(struct.pack(pattern, *self.min_state_range))
      length = len(self.max_state_range)
      buff.write(_struct_I.pack(length))
      pattern = '<%sf'%length
      buff.write(struct.pack(pattern, *self.max_state_range))
      _x = self
      buff.write(_struct_2f2B.pack(_x.max_reward, _x.reward_range, _x.stochastic, _x.episodic))
      _x = self.title
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
    except struct.error as se: self._check_types(se)
    except TypeError as te: self._check_types(te)

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    try:
      end = 0
      _x = self
      start = end
      end += 8
      (_x.num_actions, _x.num_states,) = _struct_2f.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sf'%length
      start = end
      end += struct.calcsize(pattern)
      self.min_state_range = struct.unpack(pattern, str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sf'%length
      start = end
      end += struct.calcsize(pattern)
      self.max_state_range = struct.unpack(pattern, str[start:end])
      _x = self
      start = end
      end += 10
      (_x.max_reward, _x.reward_range, _x.stochastic, _x.episodic,) = _struct_2f2B.unpack(str[start:end])
      self.stochastic = bool(self.stochastic)
      self.episodic = bool(self.episodic)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.title = str[start:end].decode('utf-8')
      else:
        self.title = str[start:end]
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill


  def serialize_numpy(self, buff, numpy):
    """
    serialize message with numpy array types into buffer
    :param buff: buffer, ``StringIO``
    :param numpy: numpy python module
    """
    try:
      _x = self
      buff.write(_struct_2f.pack(_x.num_actions, _x.num_states))
      length = len(self.min_state_range)
      buff.write(_struct_I.pack(length))
      pattern = '<%sf'%length
      buff.write(self.min_state_range.tostring())
      length = len(self.max_state_range)
      buff.write(_struct_I.pack(length))
      pattern = '<%sf'%length
      buff.write(self.max_state_range.tostring())
      _x = self
      buff.write(_struct_2f2B.pack(_x.max_reward, _x.reward_range, _x.stochastic, _x.episodic))
      _x = self.title
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
    except struct.error as se: self._check_types(se)
    except TypeError as te: self._check_types(te)

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    try:
      end = 0
      _x = self
      start = end
      end += 8
      (_x.num_actions, _x.num_states,) = _struct_2f.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sf'%length
      start = end
      end += struct.calcsize(pattern)
      self.min_state_range = numpy.frombuffer(str[start:end], dtype=numpy.float32, count=length)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sf'%length
      start = end
      end += struct.calcsize(pattern)
      self.max_state_range = numpy.frombuffer(str[start:end], dtype=numpy.float32, count=length)
      _x = self
      start = end
      end += 10
      (_x.max_reward, _x.reward_range, _x.stochastic, _x.episodic,) = _struct_2f2B.unpack(str[start:end])
      self.stochastic = bool(self.stochastic)
      self.episodic = bool(self.episodic)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.title = str[start:end].decode('utf-8')
      else:
        self.title = str[start:end]
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill

_struct_I = genpy.struct_I
_struct_2f2B = struct.Struct("<2f2B")
_struct_2f = struct.Struct("<2f")
