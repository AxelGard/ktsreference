

# getOrDefault

Returns this Optional's value if present, or otherwise defaultValue.

```kotlin
fun <T> Optional<out T & Any>.getOrDefault(defaultValue: T): T(source)
```

```kotlin
import java.util.Optional

fun main() {
    val present = Optional.of("Hello, world!")
    val absent  = Optional.empty<String>()

    val greeting1 = present.getOrDefault("Hi there")
    val greeting2 = absent.getOrDefault("Hi there")

    println(greeting1) // prints: Hello, world!
    println(greeting2) // prints: Hi there
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm.optionals/get-or-default.html)

    