/**
 * Civic Profile — Civic Growth Ladder v1.0 (Build #12)
 * Client-side level estimation from participation signals.
 */

const CIVIC_PREFIX = 'cf_civic_';

const LEVEL_ORDER = ['visitor', 'subscriber', 'advocate', 'educator', 'regional_leader', 'research_contributor', 'national_leader'];

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

function estimateCivicLevel() {
  const explicit = civicGet('level');
  if (explicit && LEVEL_ORDER.includes(explicit)) return explicit;

  const joinedNetwork = localStorage.getItem('cf_joined_network') === 'true';
  const educationLead = localStorage.getItem('cf_education_lead') === 'true';
  const shareCount = parseInt(localStorage.getItem('cf_share_count') || '0', 10);
  const halls = JSON.parse(localStorage.getItem('cf_halls_visited') || '[]');
  const hostedConversation = civicGet('hosted_conversation', false);

  if (educationLead && hostedConversation) return 'educator';
  if (educationLead) return 'educator';
  if (shareCount >= 2 || localStorage.getItem('cf_invites_sent')) return 'advocate';
  if (joinedNetwork) return 'subscriber';
  if (halls.length >= 1) return 'visitor';
  return 'visitor';
}

function civicLevelNumber(level) {
  const idx = LEVEL_ORDER.indexOf(level);
  return idx >= 0 ? idx + 1 : 1;
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
  trackShare,
  trackNetworkJoin,
  trackEducationLead,
  trackConversationHost,
  LEVEL_ORDER
};
