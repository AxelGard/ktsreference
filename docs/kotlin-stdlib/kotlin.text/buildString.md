

# buildString

Builds new string by populating newly created StringBuilder using provided builderAction and then converting it to String.

```kotlin
inline fun buildString(builderAction: StringBuilder.() -> Unit): String(source)
```

```kotlin
val message = buildString {
    append("Hello, ")
    append("world!")
    append('\n')
    append("This is a buildString example.")
}

println(message)
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.text/build-string.html)

    