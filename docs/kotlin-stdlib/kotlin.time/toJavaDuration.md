

# toJavaDuration

Converts kotlin.time.Duration value to java.time.Duration value.

```kotlin
inline fun Duration.toJavaDuration(): Duration(source)
```

```kotlin
import kotlin.time.Duration
import kotlin.time.Duration.Companion.seconds
import java.time.Duration as JavaDuration

fun main() {
    // Kotlin duration of 5 seconds
    val kotlinDuration: Duration = 5.seconds

    // Convert to java.time.Duration
    val javaDuration: JavaDuration = kotlinDuration.toJavaDuration()

    println("Kotlin Duration: $kotlinDuration")
    println("Java Duration: $javaDuration")
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.time/to-java-duration.html)

    