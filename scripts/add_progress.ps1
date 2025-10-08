param(
    [string]$Date = (Get-Date -Format yyyy-MM-dd),
    [int]$ProblemsSolved = 0,
    [string]$Topic = "",
    [string]$Status = "In Progress",
    [string]$Day = (Get-Date -Format dddd),
    [string]$File = "c:\\Shubham\\Personal work\\DSA\\Progress.md"
)

# Prepare the row (ensure pipes and escaping)
$escapedTopic = $Topic -replace '\|','\\|'
$row = "| $Date | $ProblemsSolved | $escapedTopic | $Status | $Day |"

# Append a blank line if the file doesn't end with a newline
$content = Get-Content -Path $File -Raw
if ($content -notmatch "\r?\n$") {
    Add-Content -Path $File -Value "`n"
}

# Append the row
Add-Content -Path $File -Value $row
Write-Output "Appended: $row"