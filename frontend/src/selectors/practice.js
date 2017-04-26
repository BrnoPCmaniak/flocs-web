import { getPracticePageTaskId } from '../selectors/taskEnvironment';
import { getMode } from '../selectors/app';


export function getRecommendation(state) {
  return state.recommendation;
}


export function getRecommendedTask(state) {
  const recommendation = getRecommendation(state);
  const { task, available } = recommendation;
  const taskId = task;  // TODO: make a single convention about naming id attributes
  if (!available) {
    return null;
  }
  if (getMode(state) === 'task' && getPracticePageTaskId(state) === taskId) {
    return null;
  }
  const url = `/task/${taskId}`;
  return { taskId, url };
}
