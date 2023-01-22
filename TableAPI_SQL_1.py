from pyflink.table import EnvironmentSettings, TableEnvironment 

env_settings = EnvironmentSettings.in_batch_mode()
table_env = TableEnvironment.create(env_settings)

table = table_env.from_elements([(1, 'Hi'), (2, 'Hello')])
table.execute().print() 
