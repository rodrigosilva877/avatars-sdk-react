npm install @runwayml/avatars-react
import { AvatarCall } from '@runwayml/avatars-react';

function App() {
  return (
    <AvatarCall
      avatarId="BETO""
      connectUrl="/api/avatar/connect"
    />
  );
}
