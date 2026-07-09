/**
 * Civic Profile — Arkansas Education Ladder v1.1 (Build #12)
 */

const CIVIC_PREFIX = 'cf_civic_';

const LEVEL_ORDER = [
  'visitor',
  'subscriber',
  'community_supporter',
  'educator',
  'county_leader',
  'ar_research_contributor',
  'education_council'
];

const LEGACY_MAP = {
  advocate: 'community_supporter',
  regional_leader: 'county_leader',
  research_contributor: 'ar_research_contributor',
  national_leader: 'education_council'
};

function civicGet(key, fallback = null) {
  try {
    const v = localStorage.getItem(CIVIC_PREFIX + key);
    return v === null ? fallback : JSON.parse(v);
  } catch {
    return fallback;
  }
}

function civicSet(key, value) {
  localStorage.setItem(CIVIC_PREFIX + key, JSON.stringify(value));
}

function normalizeLevel(level) {
  return LEGACY_MAP[level] || level;
}

function estimateCivicLevel() {
  const explicit = civicGet('level');
  if (explicit) {
    const norm = normalizeLevel(explicit);
    if (LEVEL_ORDER.includes(norm)) return norm;
  }

  const joinedNetwork = localStorage.getItem('cf_joined_network') === 'true';
  const educationLead = localStorage.getItem('cf_education_lead') === 'true';
  const shareCount = parseInt(localStorage.getItem('cf_share_count') || '0', 10);
  const halls = JSON.parse(localStorage.getItem('cf_halls_visited') || '[]');
  const hostedConversation = civicGet('hosted_conversation', false);
  const countyLeader = civicGet('county_leader', false);

  if (countyLeader) return 'county_leader';
  if (educationLead && hostedConversation) return 'educator';
  if (educationLead) return 'educator';
  if (shareCount >= 2 || localStorage.getItem('cf_invites_sent')) return 'community_supporter';
  if (joinedNetwork) return 'subscriber';
  if (halls.length >= 1) return 'visitor';
  return 'visitor';
}

function civicLevelNumber(level) {
  const norm = normalizeLevel(level || estimateCivicLevel());
  const idx = LEVEL_ORDER.indexOf(norm);
  return idx >= 0 ? idx + 1 : 1;
}

function getArkansasCounty() {
  return localStorage.getItem('cf_arkansas_county') || null;
}

function setArkansasCounty(county) {
  if (county) localStorage.setItem('cf_arkansas_county', county);
}

function trackShare() {
  const n = parseInt(localStorage.getItem('cf_share_count') || '0', 10) + 1;
  localStorage.setItem('cf_share_count', String(n));
}

function trackNetworkJoin() {
  localStorage.setItem('cf_joined_network', 'true');
}

function trackEducationLead() {
  localStorage.setItem('cf_education_lead', 'true');
}

function trackConversationHost() {
  civicSet('hosted_conversation', true);
}

window.CivicProfile = {
  estimateCivicLevel,
  civicLevelNumber,
  normalizeLevel,
  getArkansasCounty,
  setArkansasCounty,
  trackShare,
  trackNetworkJoin,
  trackEducationLead,
  trackConversationHost,
  LEVEL_ORDER
};
