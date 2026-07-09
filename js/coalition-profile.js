/**
 * Coalition Profile — ACUCOS v1.0 (Build #14)
 */

const COALITION_PREFIX = 'cf_coalition_';

const GROWTH_PATHWAYS = [
  'individual_referral',
  'organizational_referral',
  'event_recruitment',
  'community_conversations',
  'social_media'
];

const LEVEL_LEGACY = { community_partner: 'event_partner' };

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

function normalizeParticipationLevel(level) {
  return LEVEL_LEGACY[level] || level;
}

function markOrganizationInterest() {
  coalitionSet('interest', true);
  coalitionSet('interest_at', new Date().toISOString());
}

function markOrganizationJoined(meta = {}) {
  coalitionSet('joined', true);
  coalitionSet('joined_at', new Date().toISOString());
  if (meta.county) coalitionSet('county', meta.county);
  if (meta.level) coalitionSet('level', normalizeParticipationLevel(meta.level));
  if (meta.category) coalitionSet('category', meta.category);
  if (meta.name) coalitionSet('org_name', meta.name);
}

function trackGrowthPathway(pathwayId) {
  if (!GROWTH_PATHWAYS.includes(pathwayId)) return;
  const counts = coalitionGet('growth_pathways', {});
  counts[pathwayId] = (counts[pathwayId] || 0) + 1;
  coalitionSet('growth_pathways', counts);
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
  normalizeParticipationLevel,
  markOrganizationInterest,
  markOrganizationJoined,
  trackGrowthPathway,
  getCoalitionCounty,
  hasCoalitionInterest,
  GROWTH_PATHWAYS
};
