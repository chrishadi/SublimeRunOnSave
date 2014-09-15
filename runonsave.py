import sublime, sublime_plugin
 
class RunOnSave(sublime_plugin.EventListener):
 
  def on_post_save(self, view):
    # Check if project has run-on-save enabled.
    settings = view.settings()
    if settings.get('run_on_save') == 1:
      command = settings.get('command')
      if command is not None:
        option_dict = {'cmd': command}
        folders = view.window().folders()
        if folders is not None and len(folders) > 0:
       	  option_dict['working_dir'] = folders[0]
        path = settings.get('path')
        if path is not None:
          option_dict['path'] = path
        environment_dict = settings.get('environment_variables')
        if environment_dict is not None and len(environment_dict) > 0:
          option_dict['env'] = environment_dict;
        view.window().run_command('exec', option_dict)
