BACKEND = 'task_1.frontera.backends.ScoredBackend'
SQLALCHEMYBACKEND_ENGINE = 'sqlite:///testing_frontier.db'
SQLALCHEMYBACKEND_MODELS = {
    'ScoredPage': 'task_1.frontera.backends.ScoredPage',
}
