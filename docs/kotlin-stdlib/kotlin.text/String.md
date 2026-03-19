

# String

Warning since 1.4

```kotlin
expect fun String(chars: CharArray): String(source)
```

```kotlin
val chars = charArrayOf('H', 'e', 'l', 'l', 'o', ' ', 'K', 'o', 't', 'l', 'i', 'n')
val greeting = String(chars)
println(greeting)   // Prints: Hello Kotlin
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.text/-string.html)

    