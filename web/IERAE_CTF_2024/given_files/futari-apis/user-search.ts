type User = {
  name: string;
};

const FLAG: string = Deno.env.get("FLAG") || "IERAE{dummy}";
const PORT: number = parseInt(Deno.env.get("PORT") || "3000");

const users = new Map<string, User>();
users.set("peroro", { name: "Peroro sama" });
users.set("wavecat", { name: "Wave Cat" });
users.set("nicholai", { name: "Mr.Nicholai" });
users.set("bigbrother", { name: "Big Brother" });
users.set("pinkypaca", { name: "Pinky Paca" });
users.set("adelie", { name: "Angry Adelie" });
users.set("skullman", { name: "Skullman" });

function search(id: string) {
  const user = users.get(id);
  return user;
}

function handler(req: Request): Response {
  // API format is /:id
  const url = new URL(req.url);
  const id = url.pathname.slice(1);
  const apiKey = url.searchParams.get("apiKey") || "";

  if (apiKey !== FLAG) {
    return new Response("Invalid API Key.");
  }

  const user = search(id);
  if (!user) {
    return new Response("User not found.");
  }

  return new Response(`User ${user.name} found.`);
}

Deno.serve({ port: PORT, handler });
