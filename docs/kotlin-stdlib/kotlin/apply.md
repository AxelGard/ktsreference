

# apply

Calls the specified function block with this value as its receiver and returns this value.

```kotlin
@IgnorableReturnValueinline fun <T> T.apply(block: T.() -> Unit): T(source)
```

```kotlin
data class User(var name: String = "", var age: Int = 0)

val user = User().apply {
    name = "Alice"
    age = 30
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/apply.html)

    