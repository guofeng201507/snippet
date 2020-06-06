def remove_fc(state_dict):
    """ Remove the fc layer parameter from state_dict. """
  return {key: value for key, value in state_dict.items() if not key.startswith('fc.')}
