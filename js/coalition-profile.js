/**
 * Coalition Profile — Arkansas Organization Tracker v1.0 (Build #13)
 */

const COALITION_PREFIX = 'cf_coalition_';

function coalitionGet(key, fallback = null) {
  try {
    const v = localStorage.getItem(COALITION_PREFIX + key);
    return v === null ? fallback : JSON.parse(v);
  } catch {
    return fallback;
  }
}

function coalitionSet(key, value) {
  localStorage.setItem(COALITION_PREFIX + key, JSON.stringify(value));
}

function markOrganizationInterest() {
  coalitionSet('interest', true);
  coalitionSet('interest_at', new Date().toISOString());
}

function markOrganizationJoined(meta = {}) {
  coalitionSet('joined', true);
  coalitionSet('joined_at', new Date().toISOString());
  if (meta.county) coalitionSet('county', meta.county);
  if (meta.level) coalitionSet('level', meta.level);
  if (meta.name) coalitionSet('org_name', meta.name);
}

function getCoalitionCounty() {
  return coalitionGet('county') || localStorage.getItem('cf_arkansas_county') || null;
}

function hasCoalitionInterest() {
  return coalitionGet('interest') === true || coalitionGet('joined') === true;
}

window.CoalitionProfile = {
  get: coalitionGet,
  set: coalitionSet,
  markOrganizationInterest,
  markOrganizationJoined,
  getCoalitionCounty,
  hasCoalitionInterest
};
