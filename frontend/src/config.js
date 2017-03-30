import { createStore, applyMiddleware } from 'redux';
import thunk from 'redux-thunk';
import createPromiseMiddleware from 'redux-promise-middleware';
import createLoggerMiddleware from 'redux-logger';
import rootReducer from './reducers';
import { initGlobalBlockly } from './core/blockly';
import { initGlobalTheme } from './theme';



export function globalConfiguration() {
  initGlobalTheme();
  initGlobalBlockly();
}


export function configureStore(initialState) {
  const promise = createPromiseMiddleware();
  const logger = createLoggerMiddleware();
  const middleware = applyMiddleware(promise, thunk, logger);
  const store = createStore(rootReducer, initialState);

  if (module.hot) {
    // Enable Webpack hot module replacement for reducers
    module.hot.accept('./reducers', () => {
      const nextRootReducer = require('./reducers/index');
      store.replaceReducer(nextRootReducer);
    });
  }

  return store;
}
