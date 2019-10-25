while getopts ":e:" opt; do
  case $opt in
    e)
      if [ "$2" = "local" -o "$2" = "dev" -o "$2" = "prod" ]; then
        echo "Running the package script..."
        echo "Removing Deploy Folder"
        rm -rf ./elasticsearch/deploy
        echo "Deploy Folder Removed"
        echo "Create Deploy Folder"
        sh ./elasticsearch/scripts/package.sh
        echo "Deploy folder created"
        echo "Running cfn deploy for main stack using local config."
        cfn deploy -t elasticsearch/infrastructure/stack/main.yaml -c elasticsearch/infrastructure/$2.json --profile dhishrdsvc$2 --s3-bucket ##TODO##
        echo "To start working again, remember to run sh ./scripts/develop.sh"
      else
        echo "Invalid environment. Can only be used for local, dev, or prod"
      fi;
      ;;
    \?)
      echo "Invalid option: -$OPTARG" >&2
      echo "Use -e to set environment"
      exit 1
      ;;
    :)
      echo "Option -$OPTARG requires an argument." >&2
      echo "Invalid environment. Can only be used for local, dev, or prod"
      exit 1
      ;;
    *)
      echo "Use -e to set environment"
      echo "Can only be used for local, dev, or prod"
  esac
done