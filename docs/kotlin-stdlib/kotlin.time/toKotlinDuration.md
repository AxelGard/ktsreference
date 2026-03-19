

# toKotlinDuration

Converts java.time.Duration value to kotlin.time.Duration value.

```kotlin
inline fun Duration.toKotlinDuration(): Duration(source)
```

```kotlin
import java.time.Duration
import kotlin.time.Duration as KotlinDuration

fun main() {
    val javaDuration = Duration.ofHours(1).plusMinutes(30)
    val kotlinDuration: KotlinDuration = javaDuration.toKotlinDuration()

    println(kotlinDuration)                // PT1H30M
    println(kotlinDuration.inWholeMinutes) // 90
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.time/to-kotlin-duration.html)

    