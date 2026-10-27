"""Smoke test do ARC-AGI Toolkit usando um jogo já suportado pelo SDK."""
import os
import sys


def main() -> int:
    try:
        import arc_agi
        from arcengine import GameAction
    except ImportError as exc:
        print("Toolkit ausente. Execute: python -m pip install -r requirements.txt")
        print(f"Detalhe: {exc}")
        return 2

    game_name = os.environ.get("ARC_GAME", "ls20")
    arcade = arc_agi.Arcade()
    env = arcade.make(game_name, render_mode="terminal")
    print("Jogo:", game_name)
    print("Espaço de ações:", env.action_space)
    for action in (GameAction.ACTION1, GameAction.ACTION2):
        observation = env.step(action)
        print(f"Ação {action}: observação recebida ({type(observation).__name__})")
    print("Smoke test concluído. O ambiente oficial customizado ainda requer implementação e validação separadas.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
