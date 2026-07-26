import fs from "node:fs";
import path from "node:path";
import { fileURLToPath } from "node:url";

const pluginDir = path.dirname(fileURLToPath(import.meta.url));
const rootDir = path.resolve(pluginDir, "../..");
const skillsDir = path.join(rootDir, "skills");
const bootstrapPath = path.join(rootDir, "BOOTSTRAP.md");
const marker = "ai-knowledge-base:bootstrap";

function bootstrap() {
  if (!fs.existsSync(bootstrapPath)) return null;
  return `<AI_KNOWLEDGE_BASE_BOOTSTRAP>\n${marker}\n\n${fs.readFileSync(bootstrapPath, "utf8")}\n</AI_KNOWLEDGE_BASE_BOOTSTRAP>`;
}

export const AiKnowledgeBasePlugin = async () => ({
  config: async (config) => {
    config.skills ??= {};
    config.skills.paths ??= [];
    if (!config.skills.paths.includes(skillsDir)) config.skills.paths.push(skillsDir);
  },
  "experimental.chat.messages.transform": async (_input, output) => {
    const content = bootstrap();
    if (!content || !output.messages.length) return;
    const firstUser = output.messages.find((message) => message.info?.role === "user");
    if (!firstUser?.parts?.length) return;
    if (firstUser.parts.some((part) => part.type === "text" && part.text.includes(marker))) return;
    firstUser.parts.unshift({ ...firstUser.parts[0], type: "text", text: content });
  },
});

export default AiKnowledgeBasePlugin;
