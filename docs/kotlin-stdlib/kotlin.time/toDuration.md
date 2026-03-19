

# toDuration

Returns a Duration equal to this Int number of the specified unit.

```kotlin
fun Int.toDuration(unit: DurationUnit): Duration(source)
```

```kotlin
import kotlin.time.DurationUnit
import kotlin.time.toDuration

fun main() {
    val fiveSeconds = 5.toDuration(DurationUnit.SECONDS)
    println(fiveSeconds) // PT5S
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.time/to-duration.html)

    