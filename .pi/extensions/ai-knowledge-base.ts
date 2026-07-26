import { readFileSync } from "node:fs";
import { dirname, resolve } from "node:path";
import { fileURLToPath } from "node:url";
import type { ExtensionAPI } from "@earendil-works/pi-coding-agent";

const MARKER = "ai-knowledge-base:bootstrap";
const extensionDir = dirname(fileURLToPath(import.meta.url));
const rootDir = resolve(extensionDir, "../..");
const skillsDir = resolve(rootDir, "skills");
const bootstrapPath = resolve(rootDir, "BOOTSTRAP.md");
let cached: string | null | undefined;

function getBootstrap(): string | null {
  if (cached !== undefined) return cached;
  try {
    cached = `<AI_KNOWLEDGE_BASE_BOOTSTRAP>\n${MARKER}\n\n${readFileSync(bootstrapPath, "utf8")}\n</AI_KNOWLEDGE_BASE_BOOTSTRAP>`;
  } catch {
    cached = null;
  }
  return cached;
}

export default function aiKnowledgeBaseExtension(pi: ExtensionAPI) {
  let inject = true;
  pi.on("resources_discover", async () => ({ skillPaths: [skillsDir] }));
  pi.on("session_start", async () => { inject = true; });
  pi.on("session_compact", async () => { inject = true; });
  pi.on("agent_end", async () => { inject = false; });
  pi.on("context", async (event) => {
    if (!inject || event.messages.some((message) => JSON.stringify(message).includes(MARKER))) return;
    const content = getBootstrap();
    if (!content) return;
    return {
      messages: [
        { role: "user" as const, content: [{ type: "text" as const, text: content }], timestamp: Date.now() },
        ...event.messages,
      ],
    };
  });
}
