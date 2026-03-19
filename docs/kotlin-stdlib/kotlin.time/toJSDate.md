

# toJSDate

Converts the Instant to an instance of JS Date.

```kotlin
fun Instant.toJSDate(): Date(source)
```

```kotlin
import kotlin.time.*
import kotlin.js.Date
import kotlin.browser.*

fun main() {
    // Get the current instant from the system clock
    val instant = Clock.System.now()

    // Convert the Instant to a JavaScript Date instance
    val jsDate: Date = instant.toJSDate()

    // Log the resulting JS Date to the console
    console.log("Instant as JS Date:", jsDate)
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.time/to-j-s-date.html)

    