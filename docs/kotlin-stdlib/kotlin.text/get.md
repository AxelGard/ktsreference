

# get

Returns a named group with the specified name.

```kotlin
expect operator fun MatchGroupCollection.get(name: String): MatchGroup?(source)
```

```kotlin
import kotlin.text.*

fun main() {
    val regex = """(?<day>\d{2})/(?<month>\d{2})/(?<year>\d{4})""".toRegex()
    val text = "12/07/2024"

    val match = regex.matchEntire(text)
    val groups = match?.groups

    val day   = groups?.get("day")?.value   // "12"
    val month = groups?.get("month")?.value // "07"
    val year  = groups?.get("year")?.value  // "2024"

    println("Day: $day, Month: $month, Year: $year")
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.text/get.html)

    