<script lang="ts">
  import GameLogo from "../../components/GameLogo/+GameLogo.svelte";
</script>

<main>
  <GameLogo />

  <center>
    <h1><u><b>What is a gamedata file?</b></u></h1>
    <h2>
      A gamedata file is one of many files used by Fields of Mistria to store
      your save.
    </h2>
    <h1><u><b>Where do I find my gamedata file?</b></u></h1>
    <h2>
      Do Win+R, copy this, and hit enter:
      %USERPROFILE%/AppData/Local/FieldsOfMistria/saves. Look for the most
      recently updated .sav file, that's your most recent save. Copy it over to
      a safe location. Next, you want to download the most recent release from <a
        href="https://github.com/NPC-Studio/vaultc"
        >https://github.com/NPC-Studio/vaultc</a
      >. Run the following command on your terminal or powershell:
      path/to/vaultc-x86_64-pc-windows-msvc-v0.1.0.exe unpack
      path/to/savefile.sav outputfilename. Inside the generated zip there are
      various .json files that include gamedata.json. This is the file you want
      to input here.
    </h2>
  </center>
</main>

<style>
  @import "./+page.css";
</style>
