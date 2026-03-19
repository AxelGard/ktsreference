

# error

Throws an IllegalStateException with the given message.

```kotlin
inline fun error(message: Any): Nothing(source)
```

```kotlin
fun validateAge(age: Int) {
    if (age < 0) error("Age cannot be negative: $age")
}

fun main() {
    try {
        validateAge(-5)
    } catch (e: IllegalStateException) {
        println(e.message) // Prints: Age cannot be negative: -5
    }
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/error.html)

    