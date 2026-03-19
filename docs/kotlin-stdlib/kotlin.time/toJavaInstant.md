

# toJavaInstant

Converts this kotlin.time.Instant value to a java.time.Instant value.

```kotlin
fun Instant.toJavaInstant(): Instant(source)
```

```kotlin
import kotlin.time.Instant
import java.time.Instant as JInstant

fun main() {
    val kotlinInstant = Instant.now()
    val javaInstant: JInstant = kotlinInstant.toJavaInstant()
    println(javaInstant)   // prints the Java Instant representation
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.time/to-java-instant.html)

    