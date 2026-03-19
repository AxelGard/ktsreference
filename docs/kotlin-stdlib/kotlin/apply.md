

# apply

 [kotlin-stdlib](/kotlin-stdlib) / [kotlin](/kotlin-stdlib/kotlin) / [apply](kotlin-stdlib/kotlin/apply)

Calls the specified function block with this value as its receiver and returns this value.

```kotlin
@IgnorableReturnValueinline fun <T> T.apply(block: T.() -> Unit): T(source)
```

```kotlin
data class Person(var name: String = "", var age: Int = 0)

val person = Person().apply {
    name = "Alice"
    age = 28
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/apply.html)

    